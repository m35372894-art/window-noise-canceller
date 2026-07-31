import numpy as np

class ANCWindowSystem:
    def init(self, filter_taps=32, mu=0.01):
        """
        Инициализация активной системы шумоподавления.
        :param filter_taps: Количество коэффициентов адаптивного FIR-фильтра.
        :param mu: Скорость обучения (step size) алгоритма LMS.
        """
        self.taps = filter_taps
        self.mu = mu
        self.weights = np.zeros(filter_taps)
        self.buffer = np.zeros(filter_taps)

    def process_sample(self, noise_sample: float, error_sample: float) -> float:
        """
        Обработка одного сэмпла аудио.
        :param noise_sample: Сигнал с внешнего микрофона.
        :param error_sample: Сигнал с внутреннего микрофона (ошибка).
        :return: Сигнал противофазы для динамика.
        """
        # Сдвиг буфера и добавление нового сэмпла
        self.buffer = np.roll(self.buffer, 1)
        self.buffer[0] = noise_sample

        # Вычисление инвертированного сигнала (противофазы)
        anti_noise = np.dot(self.weights, self.buffer)

        # Обновление весов фильтра (Normalized LMS)
        norm = np.dot(self.buffer, self.buffer) + 1e-6
        self.weights += (self.mu * error_sample * self.buffer) / norm

        return -anti_noise  # Инвертированный сигнал на динамик

# Пример эмуляции работы
if name == "main":
    anc = ANCWindowSystem(filter_taps=64, mu=0.05)
    print("ANC Window Engine initialized successfully.")
    
    # Симуляция звука
    dummy_noise = 0.8
    dummy_error = 0.1
    output_signal = anc.process_sample(dummy_noise, dummy_error)
    print(f"Input Noise: {dummy_noise} -> Anti-Noise Output: {output_signal:.4f}")
