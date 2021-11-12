# Exploring eBay Car Sales Data

## About the repository
This repository contains a solution for the Guided Project: Exploring eBay Car Sales Data from DataQuest's Pandas and NumPy Fundamentals module applying clean coding skills.

### The repository tree
```
├── README.md
├── requeriments.txt
├── .pylintrc
├── config.yml
├── data
│   ├── autos.csv           
│   ├── autos_processed.csv              
│   ├── mean_price_mileage_by_brand.csv              
├── log
│   ├── etl.log               
├── notebook
│   └── prediction-of-quality-of-wine.ipynb
└── scripts           
    ├── etl.py                
    └── utils.py
```

## Setup

1. Git Clone the repo
   ```git clone https://github.com/thiagomaiasouto/Exploring-eBay-Car-Sales-Data.git```

2. Go to project root folder
   ```cd Exploring-eBay-Car-Sales-Data```

3. Setup conda env in terminal
   ```
   conda create --name YOUR_ENVIROMENT_NAME python=3.8 --file requeriments.txt

   conda activate YOUR_ENVIROMENT_NAME
   ```

4. Run the code in the terminal
   
   ```
   python ./scripts/etl.py
   ```

5. To execute pylint and analyze the code format

    ```
    pylint ./scripts
    ```

6. After usage
   
   ```
   conda deactivate
   conda remove --name YOUR_ENVIROMENT_NAME --all
   ```