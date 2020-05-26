import csv 
import re
import yfinance as yf
import sys
import os.path
import glob 
import traceback

class get_data_per_stock():
    
    def __init__(self, file_name):
        self.stock_symbols = csv.reader(open(file_name, 'r'))

    def reformat_stock_symbols_for_y_finance(self):
        self.reformated_stock_symbols = []
        for stock_symbol_row in self.stock_symbols:
            stock_symbol = stock_symbol_row[0]

            if ".CL" in stock_symbol:
                if stock_symbol == "ARRpB.CL":
                    stock_symbol = "ARR-PBCL"
                elif stock_symbol == "COFpP.CL":
                    stock_symbol = "COF-PPCL"
                elif stock_symbol == "JPMpF.CL":
                    stock_symbol = "JPM-PFCL"
                elif stock_symbol == "OSLE.CL":
                    stock_symbol = "OSLE-CL"

            elif "." in stock_symbol:
                stock_symbol = stock_symbol.split(".")[0] + "-" + stock_symbol.split(".")[1]
            elif "p" in stock_symbol:
                split_stock_symbol = stock_symbol.split("p")
                stock_symbol = split_stock_symbol[0] + "-P" + split_stock_symbol[1]

            self.reformated_stock_symbols.append(stock_symbol)

    def save_stock_history(self):
        
        for stock_symbol in self.reformated_stock_symbols:
            try:
                ticker = yf.Ticker(stock_symbol)
                sector = ticker.info['sector']
                history = ticker.history(start="2010-01-01", end="2020-03-13", auto_adjust=False)
                history.to_csv("./data/dataset_with_sector/" + stock_symbol + "_" + sector.replace(" ", "-") + ".csv")
            except:
                e = sys.exc_info()[0]
                print (stock_symbol)
                print (e)
    
    def run(self):
        print ("----- Reformatting Stock Symbols -----")
        self.reformat_stock_symbols_for_y_finance()
        print ("----- Save Stock History -----")
        self.save_stock_history()

if __name__ == "__main__":

    file_path = None
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        g_d_p_s = get_data_per_stock(file_name)
        g_d_p_s.run()
    else:
        print("Provide file path for stock symbols")