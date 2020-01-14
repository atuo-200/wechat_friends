from flask import Flask,render_template
import login

#此模块使用flask生成一个web小应用，使好友个性签名信息在页面上显示出来

app = Flask(__name__)

@app.route('/')
def get_signature():
    #获取数据并传送到index.html
    signature_list = []
    id = 1
    for friend in login.wc_login():
        
        signature_list.append({"id":id,"nick_name":friend["nick_name"],"signature":friend["signature"]})
        id = id+1
    return render_template("index.html",signature_list = signature_list)

if __name__ == '__main__':
    app.run(debug=True)


