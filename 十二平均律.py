import matplotlib.pyplot as plt
import numpy as np

def equal_temperament(fundamental_freq, n):
    return fundamental_freq * (2 ** (n / 12))

def just_intonation(fundamental_freq):
    # 纯律比例
    ratios = [1, 16/15, 9/8, 6/5, 5/4, 4/3, 45/32, 3/2, 8/5, 5/3, 16/9, 15/8, 2]
    return [fundamental_freq * ratio for ratio in ratios]

def pythagorean_tuning(fundamental_freq):
    # 五度相生律比例
    ratios = [1, 9/8, 81/64, 4/3, 3/2, 27/16, 243/128, 2, 18/8, 16/9, 128/81, 3/2, 2]
    return [fundamental_freq * ratio for ratio in ratios]

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置黑体字体
plt.rcParams['axes.unicode_minus'] = False    # 解决坐标轴负号显示问题

# 基础频率（C1，假设从261.63 Hz开始，即C4的频率除以16）
fundamental_freq = 261.63 / 16

# 十二平均律
notes = np.arange(0, 13)
equal_frequencies = equal_temperament(fundamental_freq, notes)

# 纯律
just_frequencies = just_intonation(fundamental_freq)

# 五度相生律
pythagorean_frequencies = pythagorean_tuning(fundamental_freq)

# 音符名称（假设从C1开始）
note_names = ['C1', 'C#1/Db1', 'D1', 'D#1/Eb1', 'E1', 'F1', 'F#1/Gb1', 'G1', 'G#1/Ab1', 'A1', 'A#1/Bb1', 'B1', 'C2']

# 绘图
plt.figure(figsize=(12, 8))
plt.plot(notes, equal_frequencies, 'o-', label='十二平均律')
plt.plot(notes, just_frequencies, 's-', label='纯律')
plt.plot(notes, pythagorean_frequencies, '^-', label='五度相生律')
plt.xticks(notes, note_names, rotation=45)
plt.xlabel('音符')
plt.ylabel('频率 (Hz)')
plt.title('不同音律的音符频率比较')
plt.legend()
plt.grid(True)
plt.show()
