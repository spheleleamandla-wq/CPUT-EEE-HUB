import streamlit as st
import math
import cmath

st.set_page_config(page_title="CPUT EE Student Hub", page_icon="⚡", layout="wide")

CPUT_BLUE = "#003366"; CPUT_GOLD = "#FFB81C"
st.markdown(f"""<style>
.stApp {{background: #F0F2F6; color: #000;}}
.stButton>button {{background: {CPUT_BLUE}; color: white; border-radius: 8px; border: none; padding: 10px 20px; font-weight: bold; width: 100%;}}
.header {{background: linear-gradient(90deg, {CPUT_BLUE}, #004a99); padding: 15px; border-radius: 12px; margin-bottom: 20px;}}
.header h1 {{color: white; font-size: 26px; margin: 0;}}
.header p {{color: {CPUT_GOLD}; margin: 0;}}
.result-box {{background: white; padding: 15px; border-radius: 8px; border-left: 5px solid {CPUT_GOLD}; margin-top: 10px;}}
</style>""", unsafe_allow_html=True)

st.markdown(f"""<div class="header"><h1>CPUT EE Student Hub</h1><p>All Modules. All Levels. One App.</p></div>""", unsafe_allow_html=True)

# SIDEBAR - ALL SUBJECTS
subject = st.sidebar.selectbox(
    "📚 Select Subject",
    ["🏠 Home", "📊 GPA Calculator", "📐 Mathematics", "⚡ Electrical Principles"]
)

# 1. HOME
if subject == "🏠 Home":
    st.title("Welcome Future Engineer 👷‍♀️")
    st.write("Your CPUT EE modules in one place.")
    st.write("Start with Level 1 and work your way up.")

# 2. MATHEMATICS - FULLY CODED
elif subject == "📐 Mathematics":
    st.header("Mathematics Calculators")
    level = st.radio("Choose Level:", ["Level 1: Algebra", "Level 2: Complex & Calculus"], horizontal=True)
    
    if level == "Level 1: Algebra":
        calc = st.selectbox("Pick Calculation", ["Quadratic Equation", "Simultaneous 2x2", "Matrix 2x2 Det & Inverse"])
        
        if calc == "Quadratic Equation":
            st.write("Solve: $ax^2 + bx + c = 0$")
            a=st.number_input("a", value=1.0); b=st.number_input("b", value=0.0); c=st.number_input("c", value=0.0)
            if st.button("Solve"):
                d = b**2 - 4*a*c
                if d >= 0:
                    x1 = (-b + math.sqrt(d))/(2*a); x2 = (-b - math.sqrt(d))/(2*a)
                    st.markdown(f'<div class="result-box">x1 = {x1:.3f}<br>x2 = {x2:.3f}</div>', unsafe_allow_html=True)
                else:
                    real = -b/(2*a); imag = math.sqrt(-d)/(2*a)
                    st.markdown(f'<div class="result-box">x1 = {real:.3f} + {imag:.3f}j<br>x2 = {real:.3f} - {imag:.3f}j</div>', unsafe_allow_html=True)
        
        elif calc == "Simultaneous 2x2":
            st.write("a1x + b1y = c1  and  a2x + b2y = c2")
            col1, col2 = st.columns(2)
            with col1: a1=st.number_input("a1"); b1=st.number_input("b1"); c1=st.number_input("c1")
            with col2: a2=st.number_input("a2"); b2=st.number_input("b2"); c2=st.number_input("c2")
            if st.button("Solve"):
                det = a1*b2 - a2*b1
                if det != 0:
                    x = (c1*b2 - c2*b1)/det; y = (a1*c2 - a2*c1)/det
                    st.markdown(f'<div class="result-box">x = {x:.3f}<br>y = {y:.3f}</div>', unsafe_allow_html=True)
                else: st.error("No unique solution")

        elif calc == "Matrix 2x2 Det & Inverse":
            st.write("|a b|")
            st.write("|c d|")
            a=st.number_input("a"); b=st.number_input("b"); c=st.number_input("c"); d=st.number_input("d")
            if st.button("Calculate"):
                det = a*d - b*c
                st.markdown(f'<div class="result-box">Determinant = {det:.3f}<br>Inverse = 1/{det:.3f} * |d -b|<br>                  |-c a|</div>', unsafe_allow_html=True)

    elif level == "Level 2: Complex & Calculus":
        calc = st.selectbox("Pick Calculation", ["Rect to Polar", "Polar to Rect", "Derivative x^n", "Integral x^n"])
        
        if calc == "Rect to Polar":
            real = st.number_input("Real"); imag = st.number_input("Imaginary")
            if st.button("Convert"):
                z = complex(real, imag); mag = abs(z); ang = math.degrees(cmath.phase(z))
                st.markdown(f'<div class="result-box">Magnitude = {mag:.3f}<br>Angle = {ang:.2f}°</div>', unsafe_allow_html=True)
        
        elif calc == "Polar to Rect":
            mag = st.number_input("Magnitude"); ang = st.number_input("Angle Degrees")
            if st.button("Convert"):
                rad = math.radians(ang); real = mag*math.cos(rad); imag = mag*math.sin(rad)
                st.markdown(f'<div class="result-box">Real = {real:.3f}<br>Imag = {imag:.3f}j</div>', unsafe_allow_html=True)
        
        elif calc == "Derivative x^n":
            n = st.number_input("Power n"); x = st.number_input("x value")
            if st.button("Differentiate"):
                result = n * x**(n-1)
                st.markdown(f'<div class="result-box">d/dx[x^{n}] = {n}x^{n-1}<br>At x={x}: {result:.3f}</div>', unsafe_allow_html=True)

# 3. ELECTRICAL PRINCIPLES - FULLY CODED
elif subject == "⚡ Electrical Principles":
    st.header("Electrical Principles Calculators")
    level = st.radio("Choose Level:", ["Level 1: DC Circuits", "Level 2: AC & 3-Phase"], horizontal=True)
    
    if level == "Level 1: DC Circuits":
        calc = st.selectbox("Pick Calculation", ["Ohm's Law", "Power P=VI", "Series/Parallel", "Voltage Divider"])
        
        if calc == "Ohm's Law":
            st.info("Leave the value you want to find as 0")
            V=st.number_input("Voltage V", value=0.0); I=st.number_input("Current A", value=0.0); R=st.number_input("Resistance Ω", value=0.0)
            if st.button("Calculate"):
                if V==0 and I>0 and R>0: st.markdown(f'<div class="result-box">V = I × R = {I*R:.2f} V</div>', unsafe_allow_html=True)
                elif I==0 and V>0 and R>0: st.markdown(f'<div class="result-box">I = V / R = {V/R:.2f} A</div>', unsafe_allow_html=True)
                elif R==0 and V>0 and I>0: st.markdown(f'<div class="result-box">R = V / I = {V/I:.2f} Ω</div>', unsafe_allow_html=True)
        
        elif calc == "Power P=VI":
            V=st.number_input("Voltage V"); I=st.number_input("Current A")
            if st.button("Calculate"):
                P=V*I; st.markdown(f'<div class="result-box">P = V × I = {P:.2f} W<br>Energy in 1hr = {P/1000:.3f} kWh</div>', unsafe_allow_html=True)
        
        elif calc == "Series/Parallel":
            rtype=st.radio("Connection", ["Series", "Parallel"])
            r1=st.number_input("R1 Ω"); r2=st.number_input("R2 Ω"); r3=st.number_input("R3 Ω", value=0.0)
            if st.button("Calculate"):
                if rtype=="Series": Rt = r1+r2+r3
                else: Rt = 1/(1/r1 + 1/r2 + 1/r3 if r3>0 else 1/r1 + 1/r2)
                st.markdown(f'<div class="result-box">Total Resistance = {Rt:.2f} Ω</div>', unsafe_allow_html=True)
        
        elif calc == "Voltage Divider":
            Vin=st.number_input("Vin V"); R1=st.number_input("R1 Ω"); R2=st.number_input("R2 Ω")
            if st.button("Calculate"):
                Vout = Vin * R2 / (R1+R2)
                st.markdown(f'<div class="result-box">Vout = Vin × R2/(R1+R2) = {Vout:.2f} V</div>', unsafe_allow_html=True)

    elif level == "Level 2: AC & 3-Phase":
        calc = st.selectbox("Pick Calculation", ["Impedance Z", "3-Phase Power", "Power Factor", "Resonance"])
        
        if calc == "Impedance Z":
            R=st.number_input("R Ω"); XL=st.number_input("XL Ω"); XC=st.number_input("XC Ω")
            if st.button("Calculate"):
                X = XL - XC; Z = math.sqrt(R**2 + X**2); angle = math.degrees(math.atan2(X,R))
                st.markdown(f'<div class="result-box">Z = {Z:.2f} ∠{angle:.2f}° Ω</div>', unsafe_allow_html=True)
        
        elif calc == "3-Phase Power":
            Vl=st.number_input("Line Voltage VL V"); Il=st.number_input("Line Current IL A"); pf=st.number_input("Power Factor", max_value=1.0, value=0.8)
            if st.button("Calculate"):
                P = math.sqrt(3) * Vl * Il * pf
                S = math.sqrt(3) * Vl * Il / 1000
                st.markdown(f'<div class="result-box">Real Power P = {P/1000:.2f} kW<br>Apparent Power S = {S:.2f} kVA</div>', unsafe_allow_html=True)

        elif calc == "Power Factor":
            P=st.number_input("Real Power P kW"); S=st.number_input("Apparent Power S kVA")
            if st.button("Calculate"):
                pf=P/S; angle=math.degrees(math.acos(pf))
                st.markdown(f'<div class="result-box">PF = {pf:.3f}<br>Angle = {angle:.2f}°</div>', unsafe_allow_html=True)

# 4. GPA
elif subject == "📊 GPA Calculator":
    st.header("GPA Calculator")
    st.write("Add your modules and grades here")