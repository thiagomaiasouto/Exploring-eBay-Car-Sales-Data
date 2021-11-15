# Exploring eBay Car Sales Data

## About the repository
This project was developed with the main objetive of using new data science skills and clean code to peform a better professional portfolio for the students of DCA0305 PROJETO DE SISTEMAS BASEADOS EM APRENDIZADO DE MÁQUINA in UFRN(Universidade Federal do Rio Grande do Norte). 

The project was based on a dataset about cars on ebay called eBay Kleinanzeigen which was originally uploaded on Kaggle and was modified on dataquest.io project to perform more hurdles to the students, like unusual and null values, bad columns names and wrong infered columns type by pandas package. After manage to identify and describe the dataset, it was cleaned, reajusted and in the end some new interesting variables were found like the top 6  brands on ebay, mean prices and mean mileages per brand. The steps are described below.

- Step 1: All the columns have been renamed to a snake case pattern and some other columns have been renamed to accurately describe the columns.

- Step 2: All characters contained in the values of the columns of  price and mileage that interfered in the automatic detection of types were removed to perform the conversion to integer type of these columns.

- Step 3: Unsual and null values were removed to avoid unrealistic visualization on our analyses, for example in the column ``registration_year``, some cars used to be registred in future or before cars were invented.

- Step 4: The Top 6 brands on ebay dataset were filtered for a better look on the sales behavior.

- Step 5: A new dataframe with the mean prices and mileages of the cars in top 6 brands had been done.

- Step 6: A conversion from notebook to scripts were done using clean code techniques like the use of pep8 with pylint (obtaining a 10/10 score) which make the code more readable, the use of logger files and best practices for structuring data science projects following that [guide](https://towardsdatascience.com/from-jupyter-notebook-to-sc-582978d3c0c.

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
|   ├── images
|   |    ├── car_sales.jpg   
│   └── Exploring_eBay_Car_Sales.ipynb
└── scripts           
    ├── etl.py                
    └── utils.py
```

## Setup

1. Git Clone the repo
   ```
   git clone https://github.com/thiagomaiasouto/Exploring-eBay-Car-Sales-Data.git
   ```

2. Go to project root folder
   ```
   cd Exploring-eBay-Car-Sales-Data
   ```

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

## Authors
- [Arthur Cunha](https://github.com/arthurfpcl22)
- [Thiago Maia](https://github.com/thiagomaiasouto)

## Credits
The overall structure of the project was heavily influenced by this [article](https://towardsdatascience.com/from-jupyter-notebook-to-sc-582978d3c0c).