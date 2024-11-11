# Example - 1 

def Acount(actId,actType,actHolder,actBalence,actCreateDate):
    print(f'actId = {actId}')
    print(f'acttype = {actType}')
    print(f'actHolder = {actHolder}')
    print(f'actBalance = {actBalence}')
    print(f'actCreateDate = {actCreateDate}')
    
    
    return{
        'act-id': 'actId',
        'act-type': 'actType',
        'act-holder': 'actHolder',
        'act-balance': 'actbBalence',
        'act-create-date': 'actCreatedate'
    }
    
    Acount1 = Acount(11,'Credit','Tirsha Dixit',5000,'01/01/2020')
    print(f'Acount1 = {Acount1}')
    
    print('-------------------------')
    
# Example - 2
    
def Payment(payId,loanId,payAmount,payDate,payMethod,payStatus ):
     print(f'payId= {payId}')
     print(f'loanId= {loanId}')
     print(f'payAmount ={payAmount}')
     print(f'payDate = {payDate}')
     print(f'payMethod ={payMethod}')
     print(f'payStatus = {payStatus}')
     
     return {
         'pay-id': 'pay Id',
         'loan-id': 'loanId',
         'pay-amount': 'payAmount',
         'pay-date': 'payDate',
         'pay-method': 'payMethod',
         'pay-status':'payStatus'
     }
     
     Payment1 = pay(22,4333,5000,'01/01/2021','Credit Card','Completed')
     print(f'Payment1={Payment1}')