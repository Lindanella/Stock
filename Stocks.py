#CS175L
#stocks
commission_rate_p= float(input("Enter commission rate percentage on stock purchase:"))
commission_rate_s= float(input("Enter commission rate percentage on stock sale:"))
num_shares=float(input("Enter number of shares purchased:")) 
num_share_s=float(input("Enter number of shares sold:")) 
purchase_price= float(input("Enter purchase price per share:")) 
selling_price=float(input("Enter sell price per share:"))

amountPaidForStock=num_shares*purchase_price
purchaseCommission= commission_rate_s*amountPaidForStock
totalPaid= amountPaidForStock + purchaseCommission
stockSoldFor= num_shares * selling_price
sellingCommission= commission_rate_s*stockSoldFor
totalReceived=stockSoldFor-sellingCommission
profitOrLoss=totalReceived - totalPaid
print(f'Amount paid for the stock:${amountPaidForStock}')
print(f'Commission paid on the purchase:${purchaseCommission}')
print(f'Amount the stock sold for:$ {stockSoldFor}')
print(f' Commission paid on the sale:${sellingCommission}')
print(f' Profit (or loss if negative):$ {profitOrLoss}') 
      

