from pyscript import Element

Elements={"H": ("Hydroen(H)", 1, 1.008), 
        "He": ("Helium(H)", 2, 4.0026), 
        "C": ("Carbon(C)", 6, 12.011) , 
        "N": ("Nitrogen(N)", 7, 14.007),
        "O": ("Oxygen(O)", 8, 15.999),
        "F": ("Flurine(F)", 9, 18.998),
        "N": ("Neon(N)", 10, 20.180),
        "p": ("Phosphorus(P)", 15, 30.974),
        "S": ("Sulfur(S)", 16, 32.07),
        "CI": ("Chlorine(CI)", 17, 35.45),
        "Ar": ("Argon(Ar)", 18, 39.9),
        "Se": ("Selenium(Se)", 34, 78.97)
        } 
       
def search_element(e): 
    element1 = document.getElement("element1").value
    
    results = element.get(element1, ("element not found", "-", "-"))

    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = results[0]
    document.getElementById("atomic number").innerText = results[1]
    document.getElementById("atomic mass").innerText = results[2]