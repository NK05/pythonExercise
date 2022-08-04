import json

f = open('links.json')
  
# returns JSON object as 
# a dictionary
with open('links.json', 'r') as f:
    data = json.load(f)


# creating the recursive function
def indent(data_val,a):

    if type(data_val) is dict:
        a = a + '   '
        for i in data_val:
            
            print(a+i)
            indent(data_val[i],a)
    

indent(data,'')









                



        

      





  


  



