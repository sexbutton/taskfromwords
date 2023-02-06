import requests

def mainfunc(code):
    s = code
    def preobrazovatel(strk):
        return int(strk[0]) * strk[2:-1]

    def prv(strk):
        data = strk
    
        result = ""
        delete = ""
        result += data[:2]
        delete = data[:2]
        data = data.replace(data[:2], "")
    
        while(data != ""):
            if data[0].isalpha():
                result += data[0]
                delete += data[0]
                data = data.replace(data[0], "")
            elif data[0].isdigit():
                ar = prv(data)
                result += ar[0]
                delete += ar[1]
                data = data.replace(ar[1], "")
            elif data[0] == "}":
                result += data[0]
                delete += data[0]
                result = preobrazovatel(result)
                break
        return (result, delete)
    
    rr = ""

    while(s != ""):
        if s[0].isdigit():
            arr = prv(s)
            rr += arr[0]
            s = s.replace(arr[1], "", 1)
        else:
            rr += s[0]
            s = s.replace(s[0], "", 1)
        
    return rr

code = mainfunc("ab2{g}3{a2{fg}}")
    
response = requests.post('https://nodus.caseguru.ru/trainee/tasks', json={"task": 3, "result": code})
print(response.content)
    