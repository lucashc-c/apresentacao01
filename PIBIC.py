import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="centered")

#################### Titulos
st.title("APRESENTAÇÃO DE RESULTADOS")
st.write("")
st.write("Lucas Henrique Cabral")
st.write("LccMat")
st.write("")
st.write("")
st.header("PIBIC_NANOSCROLLS")
st.write("")


#################### codigo

st.subheader("código para criação de nanoscrolls")

codigo = """
import numpy as np

def gerar_scroll(input = "inicial.xyz",
        output = "saida.xyz",
        volt = 2.5,
	   dist = - 3.4,
        plan = 0.2,
        ang = 30):

    atms = []
    coords = []
    with open(input, "r") as f:
        linhas = f.readlines()
        for linha in linhas[2:]:
            parts = linha.split()
            atms.append(parts[0])
            coords.append([float(parts[1]), float(parts[2]), float(parts[3])])
            
    coords = np.array(coords)
    
    alpha = np.radians(ang)
    cos_a = np.cos(alpha)
    sin_a = np.sin(alpha)

    R_mat = np.array([
        [cos_a, -sin_a, 0],
        [sin_a,  cos_a, 0],
        [0,      0,     1]])

    coords_rot = coords @ R_mat
    
    x_min = coords_rot[:,0].min()
    x_max = coords_rot[:,0].max()
    L = x_max - x_min
    x_c = x_min + plan * L
    L_curvo = x_max - x_c

    a = dist / (2*np.pi)
    theta_max = volt * 2*np.pi
    R0 = (L_curvo - 0.5 * a * theta_max **2) / theta_max

    scroll_coords = []
    for x, y, z in coords_rot:
        if x <= x_c:
             scroll_coords.append([x, y, z])
        else:
            s = x - x_c         
            A = 0.5*a
            B = R0
            C = -s
            theta = (-B + np.sqrt(B**2 - 4*A*C)) / (2*A)
            R = R0 + a*theta
            nx = x_c + R*np.sin(theta)
            ny = y
            nz = R*(1 - np.cos(theta)) - a * theta
            scroll_coords.append([nx, ny, nz])

    scroll_coords = np.array(scroll_coords)
    R_inv = R_mat.T
    final_coords = scroll_coords @ R_inv

    with open(output, "w") as f:
        f.write(f"{len(atms)}\n")
        f.write(f"gerado com: angulo={ang}\n")
        for i in range(len(atms)):
            x, y, z = final_coords[i]
            f.write(f"{atms[i]:2s} {x:12.6f} {y:12.6f} {z:12.6f}\n")
            
"""
codigo2 =("""
scroll 1 gerado com 0.1 voltas
scroll 2 gerado com 0.2 voltas
scroll 3 gerado com 0.30000000000000004 voltas
scroll 4 gerado com 0.4 voltas
scroll 5 gerado com 0.5 voltas
scroll 6 gerado com 0.6000000000000001 voltas
scroll 7 gerado com 0.7000000000000001 voltas
scroll 8 gerado com 0.8 voltas
scroll 9 gerado com 0.9 voltas
scroll 10 gerado com 1.0 voltas
scroll 11 gerado com 1.1 voltas
scroll 12 gerado com 1.2000000000000002 voltas
scroll 13 gerado com 1.7 voltas
scroll 14 gerado com 2.2 voltas
scroll 15 gerado com 2.7 voltas
total de 15 criados""")
st.code(codigo, language="python")
st.code(codigo2, language="python")

################# dados dos graficos #########################################

def plotar(y, titulo):
    eixo = np.arange(1, 16)

    plt.figure(figsize=(10, 6))
    plt.plot(eixo, y, 'o-')
    plt.xlabel("scroll", fontsize=14)
    plt.xticks(eixo) 
    plt.ylabel(r"$\Delta E = \frac{E_{config} - E_{plana}}{N_{atomos}}$", fontsize=14)
    plt.ylim(-0.035, 0.001) 

    plt.title(titulo, fontsize=18)
    plt.grid(True, linestyle='--')
    plt.legend()

    # Renderização no Streamlit
    st.pyplot(plt)
    plt.clf()

def plotar2(y, titulo):
    eixo = np.arange(1, 16)

    plt.figure(figsize=(10, 6))
    plt.plot(eixo, y, 'o-')
    plt.xlabel("scroll", fontsize=14)
    plt.xticks(eixo) 
    plt.ylabel(r"$\Delta E = \frac{E_{config} - E_{plana}}{N_{atomos}}$", fontsize=14)
    #plt.ylim(-0.035, 0.001) 

    plt.title(titulo, fontsize=18)
    plt.grid(True, linestyle='--')
    plt.legend()

    # Renderização no Streamlit
    st.pyplot(plt)
    plt.clf()

airebo_c0_a0 = np.array([4.37063e-06, 1.50544e-05, 1.84538e-05, 3.30225e-05, 4.2735e-05, 4.90482e-05, 6.70163e-05, 7.04157e-05, 0.000105866, -0.001616647, -0.019132673, -0.021748737, -0.027913753, -0.030820707, -0.030059732])

airebo_c30_a0 = np.array([1.79681e-05, 1.554e-05, 2.7195e-05, 5.09907e-05, 6.94444e-05, 0.000106352, 0.000154915, 0.00018988, -0.002830225, -0.015115093, -0.016876943, -0.018186189, -0.023114802, -0.026586053, -0.029045746])

airebo_c60_a0 = np.array([1.50544e-05, 9.71251e-07, 1.26263e-05, 2.13675e-05, 3.35082e-05, 5.39044e-05, 9.17832e-05, 0.000131119, -0.008535354, -0.012544192, -0.01354798, -0.014426962, -0.016741939, -0.01841249, -0.019067599])
    
reaxff_c0_a0 = np.array([-0.00355, 0.039078, 0.015414, 0.036553, 0.057692, 0.018318, 0.034251, -0.2993, 0.031784, -0.08288, -0.20158, -0.36848, -0.81417, -0.90563, -0.99104])

reaxff_c30_a0 = np.array([0.045964, 0.054915, 0.001967, 0.001807, 0.014243, 0.043973, 0.069095, -0.16905, 0.054283, -0.16962, -0.24684, -0.28317, -0.52268, -0.52268, -0.52268])

airebo_c0_a30 = np.array([-2.42813E-06, 2.91375E-06, 3.885E-06, 8.74126E-06, 1.11694E-05, 
    2.28244E-05, 4.12782E-05, 5.97319E-05, 5.87607E-05, 7.33294E-05, 
    0.000103438, 0.000123349, -0.017866647, -0.022435412, -0.024946581 ])
    
reaxff_c0_a30 = np.array([-0.00355, 0.039078, 0.015414, 0.036553, 0.057692, 0.018318, 0.034251, -0.2993, 0.031784, -0.08288, -0.20158, -0.36848, -0.81417, -0.90563, -0.99104])
# modificar o de cima ....

######################################## apresentacao resultados nanoscrolls


st.subheader("Gráficos")

#######################################################################
st.write("Monocamada 100% plana com angulo de 0 graus")

col1, col2 = st.columns(2)

with col1:
    plotar(airebo_c0_a0, 'Airebo_plan0') 

with col2:
    plotar2(reaxff_c0_a0, 'Reaxff_plan0')

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

#######################################################################  

    
st.write("Monocamada 30% plana com angulo de 0 graus")

col1, col2 = st.columns(2)

with col1:
    plotar(airebo_c30_a0, 'Airebo_plan30') 

with col2:
    plotar2(reaxff_c30_a0, 'Reaxff_plan30')

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


#######################################################################  


st.write("Monocamada 50% plana com angulo de 0 graus")
col1, col2 = st.columns(2)

with col1:
    plotar(airebo_c60_a0, 'Airebo_plan60') 

with col2:
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.write("Não realizado")
    
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


#######################################################################  



st.write("Monocamada 100% plana com um angulo de 30 graus")
col1, col2 = st.columns(2)

with col1:
    plotar(airebo_c0_a30, 'Airebo_ang30') 

with col2:
    plotar2(reaxff_c0_a30, 'Reaxff_ang30')
    
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

#######################################################################  
    
st.subheader("Imagens")


col1, col2 = st.columns(2)

with col1:
    st.image("scroll12-ang30-plan2.png")
     

with col2:
  
    st.image("scroll10-ang0-pl50.png")
    


















    
    
    
    
    
    
    
    
    
    

