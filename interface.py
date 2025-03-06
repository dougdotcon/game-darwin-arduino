import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import json
import os

class ArduinoMouseController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Controlador de Mouse Arduino")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Configurações padrão
        self.config = {
            "resolution": {"width": 1920, "height": 1080},
            "scale": {"x": 1.0, "y": 1.0},
            "port": "",
            "baud_rate": 115200
        }
        
        self.serial = None
        self.load_config()
        self.create_gui()
        
    def load_config(self):
        try:
            if os.path.exists("config.json"):
                with open("config.json", "r") as f:
                    self.config.update(json.load(f))
        except:
            pass
            
    def save_config(self):
        try:
            with open("config.json", "w") as f:
                json.dump(self.config, f, indent=4)
        except:
            messagebox.showerror("Erro", "Não foi possível salvar as configurações")
    
    def create_gui(self):
        # Estilo
        style = ttk.Style()
        style.configure("TButton", padding=5)
        style.configure("TLabel", padding=5)
        style.configure("TFrame", padding=5)
        
        # Container principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Seção de Conexão
        connection_frame = ttk.LabelFrame(main_frame, text="Conexão Arduino", padding=10)
        connection_frame.pack(fill=tk.X, pady=5)
        
        # Porta Serial
        ttk.Label(connection_frame, text="Porta:").pack(side=tk.LEFT)
        self.port_var = tk.StringVar(value=self.config["port"])
        self.port_combo = ttk.Combobox(connection_frame, textvariable=self.port_var)
        self.port_combo.pack(side=tk.LEFT, padx=5)
        
        # Botão Atualizar Portas
        ttk.Button(connection_frame, text="Atualizar Portas", 
                  command=self.update_ports).pack(side=tk.LEFT, padx=5)
        
        # Botão Conectar
        self.connect_btn = ttk.Button(connection_frame, text="Conectar", 
                                    command=self.toggle_connection)
        self.connect_btn.pack(side=tk.LEFT, padx=5)
        
        # Seção de Configuração
        config_frame = ttk.LabelFrame(main_frame, text="Configurações", padding=10)
        config_frame.pack(fill=tk.X, pady=5)
        
        # Resolução
        res_frame = ttk.Frame(config_frame)
        res_frame.pack(fill=tk.X)
        
        ttk.Label(res_frame, text="Resolução:").pack(side=tk.LEFT)
        self.width_var = tk.StringVar(value=str(self.config["resolution"]["width"]))
        ttk.Entry(res_frame, textvariable=self.width_var, width=6).pack(side=tk.LEFT, padx=2)
        ttk.Label(res_frame, text="x").pack(side=tk.LEFT, padx=2)
        self.height_var = tk.StringVar(value=str(self.config["resolution"]["height"]))
        ttk.Entry(res_frame, textvariable=self.height_var, width=6).pack(side=tk.LEFT, padx=2)
        
        # Escala
        scale_frame = ttk.Frame(config_frame)
        scale_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(scale_frame, text="Escala X:").pack(side=tk.LEFT)
        self.scale_x_var = tk.StringVar(value=str(self.config["scale"]["x"]))
        ttk.Entry(scale_frame, textvariable=self.scale_x_var, width=6).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(scale_frame, text="Escala Y:").pack(side=tk.LEFT, padx=5)
        self.scale_y_var = tk.StringVar(value=str(self.config["scale"]["y"]))
        ttk.Entry(scale_frame, textvariable=self.scale_y_var, width=6).pack(side=tk.LEFT, padx=2)
        
        # Botão Salvar Configurações
        ttk.Button(config_frame, text="Salvar Configurações", 
                  command=self.save_settings).pack(pady=5)
        
        # Área de Teste
        test_frame = ttk.LabelFrame(main_frame, text="Área de Teste", padding=10)
        test_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Canvas para visualização
        self.canvas = tk.Canvas(test_frame, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind eventos do mouse
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Configure>", self.on_canvas_resize)
        
        # Botões de Teste
        button_frame = ttk.Frame(test_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(button_frame, text="Calibrar Mouse", 
                  command=self.calibrate_mouse).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Testar Movimento Aleatório", 
                  command=self.test_random_movement).pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Desconectado")
        status_label = ttk.Label(self.root, textvariable=self.status_var, 
                               relief=tk.SUNKEN, anchor=tk.W)
        status_label.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Inicializa a lista de portas
        self.update_ports()
    
    def update_ports(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.port_combo["values"] = ports
        if ports and not self.port_var.get():
            self.port_var.set(ports[0])
    
    def toggle_connection(self):
        if self.serial is None or not self.serial.is_open:
            try:
                self.serial = serial.Serial(
                    port=self.port_var.get(),
                    baudrate=self.config["baud_rate"],
                    timeout=1
                )
                self.connect_btn.configure(text="Desconectar")
                self.status_var.set(f"Conectado em {self.port_var.get()}")
            except Exception as e:
                messagebox.showerror("Erro de Conexão", str(e))
        else:
            try:
                self.serial.close()
            finally:
                self.serial = None
                self.connect_btn.configure(text="Conectar")
                self.status_var.set("Desconectado")
    
    def save_settings(self):
        try:
            self.config["resolution"]["width"] = int(self.width_var.get())
            self.config["resolution"]["height"] = int(self.height_var.get())
            self.config["scale"]["x"] = float(self.scale_x_var.get())
            self.config["scale"]["y"] = float(self.scale_y_var.get())
            self.config["port"] = self.port_var.get()
            
            self.save_config()
            
            if self.serial and self.serial.is_open:
                self.send_command(f"SCALE {self.config['scale']['x']} {self.config['scale']['y']}")
            
            messagebox.showinfo("Sucesso", "Configurações salvas com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", "Valores inválidos nas configurações")
    
    def send_command(self, cmd):
        if self.serial and self.serial.is_open:
            try:
                self.serial.write(f"{cmd}\n".encode())
                return True
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao enviar comando: {str(e)}")
                return False
        else:
            messagebox.showwarning("Aviso", "Arduino não está conectado")
            return False
    
    def calibrate_mouse(self):
        if self.send_command("GOTO 0 0"):
            self.status_var.set("Mouse calibrado")
    
    def on_canvas_click(self, event):
        if not self.serial or not self.serial.is_open:
            messagebox.showwarning("Aviso", "Conecte o Arduino primeiro")
            return
            
        # Converte coordenadas do canvas para coordenadas da tela
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        x_ratio = self.config["resolution"]["width"] / canvas_width
        y_ratio = self.config["resolution"]["height"] / canvas_height
        
        target_x = int(event.x * x_ratio)
        target_y = int(event.y * y_ratio)
        
        self.send_command(f"GOTO {target_x} {target_y}")
        self.status_var.set(f"Movendo para ({target_x}, {target_y})")
    
    def on_canvas_resize(self, event):
        # Atualiza as linhas de grade quando o canvas é redimensionado
        self.canvas.delete("grid")
        
        # Desenha linhas de grade
        width = event.width
        height = event.height
        
        # Linhas horizontais
        for i in range(0, height, 50):
            self.canvas.create_line(0, i, width, i, fill="#eee", tags="grid")
            
        # Linhas verticais
        for i in range(0, width, 50):
            self.canvas.create_line(i, 0, i, height, fill="#eee", tags="grid")
    
    def test_random_movement(self):
        import random
        x = random.randint(0, self.config["resolution"]["width"])
        y = random.randint(0, self.config["resolution"]["height"])
        if self.send_command(f"GOTO {x} {y}"):
            self.status_var.set(f"Teste: Movendo para ({x}, {y})")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ArduinoMouseController()
    app.run() 