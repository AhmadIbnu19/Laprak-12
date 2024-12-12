import pandas as pd

def tulis_file_csv():
    data = {
        "Negara": ["Indonesia", "Jepang", "Brazil", "Meksiko", "Jerman", "Inggris"],
        "Luas Area": [1905, 377, 8515, 1964, 357, 242],
        "Total Populasi": [264, 143, 210, 126, 83, 66]
    }
    df = pd.DataFrame(data)

    mean_df = df.mean(numeric_only=True).to_frame(name="Mean")
    std_df = df.std(numeric_only=True).to_frame(name="Standar Deviasi")

    mean_df.to_csv("NegaraMean.csv", index_label="Keterangan")
    std_df.to_csv("NegaraStandarDeviasi.csv", index_label="Keterangan")

    print("File NegaraMean.csv dan NegaraStandarDeviasi.csv berhasil dibuat.")
    
    print("\nIsi dari NegaraStandarDeviasi.csv:")
    std_dev_data = pd.read_csv('NegaraStandarDeviasi.csv')
    print(std_dev_data)
    
    print("\nIsi dari NegaraMean.csv:")
    mean_data = pd.read_csv('NegaraMean.csv')
    print(mean_data)

tulis_file_csv()
