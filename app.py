import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def alias_frequency(f_signal: float, fs: float) -> float:
    """
    見かけの周波数（エイリアス周波数）を 0 ～ fs/2 に折り返して返す。
    """
    if fs <= 0:
        return 0.0
    return abs(((f_signal + fs / 2) % fs) - fs / 2)


st.set_page_config(page_title="Sampling Alias Demo", layout="centered")

st.title("Sampling / Aliasing Demo")
st.write("サンプリング周波数と信号周波数の関係を、直感的に確認するミニデモです。")

st.sidebar.header("Parameters")

f_signal = st.sidebar.slider(
    "信号周波数 f_signal [Hz]",
    min_value=1,
    max_value=30,
    value=12,
    step=1,
)

fs = st.sidebar.slider(
    "サンプリング周波数 fs [Hz]",
    min_value=4,
    max_value=40,
    value=10,
    step=1,
)

duration = st.sidebar.slider(
    "表示時間 [秒]",
    min_value=1.0,
    max_value=3.0,
    value=1.5,
    step=0.1,
)

# 連続波っぽく見せるための高密度時間軸
t_cont = np.linspace(0, duration, 2000)
y_cont = np.sin(2 * np.pi * f_signal * t_cont)

# サンプル点
t_sample = np.arange(0, duration, 1 / fs)
y_sample = np.sin(2 * np.pi * f_signal * t_sample)

# エイリアス周波数
f_alias = alias_frequency(float(f_signal), float(fs))
nyquist = fs / 2

col1, col2 = st.columns(2)
col1.metric("ナイキスト周波数", f"{nyquist:.2f} Hz")
col2.metric("見かけの周波数", f"{f_alias:.2f} Hz")

if f_signal <= nyquist:
    st.success("f_signal <= fs/2 なので、ナイキスト条件の範囲内です。折り返しは起こりにくい状態です。")
else:
    st.warning("f_signal > fs/2 なので、エイリアシングが起こります。高い周波数が低い周波数に見えてしまいます。")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t_cont, y_cont, label=f"Original signal ({f_signal} Hz)")
ax.scatter(t_sample, y_sample, label=f"Sampled points (fs={fs} Hz)", s=35)
ax.plot(t_sample, y_sample, alpha=0.6, linestyle="--", label="Sampled shape")

ax.set_title("Signal and Sampled Points")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")
ax.grid(True, alpha=0.3)
ax.legend()

st.pyplot(fig)

st.subheader("What is happening?")
st.write(
    f"""
- 元の信号周波数: **{f_signal} Hz**
- サンプリング周波数: **{fs} Hz**
- ナイキスト周波数: **{nyquist:.2f} Hz**
- 見かけの周波数: **{f_alias:.2f} Hz**
"""
)

if f_signal > nyquist:
    st.write(
        "今回の設定では、サンプリング周波数の半分を超えているため、"
        "元の高い周波数が、より低い周波数として折り返して観測されます。"
    )
else:
    st.write(
        "今回の設定では、信号周波数がナイキスト周波数以下なので、"
        "サンプル点は元の波を比較的素直に表現できます。"
    )

st.markdown("---")
st.caption("Made for DSP / Speech AI study.")