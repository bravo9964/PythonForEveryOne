import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao1 = {'color':'green','dis':100}
tao.color(tao1['color'])
def rect(tao_object,tdict):
    for i in range(4):
        tao_object.forward(tdict['dis'])
        tao_object.left(90)
rect(tao,tao1)
tao2 = turtle.Pen()
tao2dict = {'color':'red','dis':50}
tao2.color(tao2dict['color'])
rect(tao2,tao2dict)


# เรียนถึง 20:22
# เปิดเต่าแล้วแว๊บหายไปเลย วิธีแก้
# dict จะใช้เก็บคีย์และแวลู คีย์ต้องไม่ซ้ำกัน ถ้ามีซ้ำกันจะเป็นการทดแทนตัวล่าสุดเข้าไป
# dict ส่วนใหญ่จะใช้กับเบอร์โทรศัพท์ หรือ ID card