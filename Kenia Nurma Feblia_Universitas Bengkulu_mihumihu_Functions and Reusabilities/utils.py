def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()
    
    # Validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan harus C, F, atau K."
    
    # Validasi nilai
    if dari == "k" and nilai < 0:
        return "Error: Nilai Kelvin tidak boleh negatif."
    
    # Konversi ke Celsius dulu
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    else:  # dari == "k"
        c = nilai - 273.15
    
    # Konversi dari Celsius ke satuan tujuan
    if ke == "c":
        return c
    elif ke == "f":
        return (c * 9/5) + 32
    else:  # ke == "k"
        return c + 273.15
