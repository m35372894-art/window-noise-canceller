import numpy as np

class AeroSilenceFXLMS:
    """
    Ultra-low latency Filtered-X LMS Adaptive Attenuator Engine.
    Designed for real-time open-window active noise control.
    """
    def init(self, filter_order: int = 64, mu: float = 0.008, leakage: float = 0.999):
        self.N = filter_order
        self.mu = mu
        self.leakage = leakage
        
        self.w = np.zeros(self.N, dtype=np.float32)
        self.s = np.zeros(self.N, dtype=np.float32)
        self.s[0] = 1.0
        
        self.x_buf = np.zeros(self.N, dtype=np.float32)
        self.fx_buf = np.zeros(self.N, dtype=np.float32)

    def process_frame(self, ref_sample: float, err_sample: float) -> float:
        self.x_buf = np.roll(self.x_buf, 1)
        self.x_buf[0] = ref_sample

        filtered_x = np.dot(self.s, self.x_buf)
        self.fx_buf = np.roll(self.fx_buf, 1)
        self.fx_buf[0] = filtered_x

        anti_noise = np.dot(self.w, self.x_buf)

        norm_power = np.dot(self.fx_buf, self.fx_buf) + 1e-5
        self.w = (self.leakage * self.w) + ((self.mu * err_sample * self.fx_buf) / norm_power)

        return -anti_noise

if name == "main":
    engine = AeroSilenceFXLMS(filter_order=64, mu=0.01)
    print("🚀 AeroSilence-ANC Engine initialized successfully.")
    output = engine.process_frame(ref_sample=0.45, err_sample=0.02)
    print(f"Anti-Noise Signal Generated: {output:.5f}")
