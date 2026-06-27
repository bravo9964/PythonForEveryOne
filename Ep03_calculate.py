tilecolor = {'red':100,'gold':200,'white':90}
print('--------โปรแกรมคำนวณจำนวณกระเบื้อง-------')
try:
    tiles = int(input('คุณมีกระเบื้องกี่แผ่น : ')) #จำนวนกระเบื้องที่มีทั้งหมด
    row =int(input('หนึ่งแถวปูกระเบื้องได้กี่แผ่น : ')) #จำนวนแผ่นต่อแถว
    color = input('กระเบื้องสีอะไร? [red/gold/white] : ')
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น')
    tiles = int(input('คุณมีกระเบื้องกี่แผ่น : ')) #จำนวนกระเบื้องที่มีทั้งหมด
    row =int(input('หนึ่งแถวปูกระเบื้องได้กี่แผ่น : ')) #จำนวนแผ่นต่อแถว
    color = input('กระเบื้องสีอะไร? [red/gold/white] : ')
#การใส่เข้าไปชุดคำสั่งเลือกคลุมข้อความแล้วกด TAB ได้เลย
total_row=tiles//row #คำนวณจำนวนแผ่นที่ใช้
remain_tiles = tiles % row # คำนวณแผ่นที่เหลือ
#print(total_row,remain_tiles)
buy_more = row - remain_tiles
print(f'มีกระเบื้องทั้งหมด: {tiles} แผ่น')
print(f'1แถวปูกระเบื้องได้: {row} แผ่น')
print('---------คำนวณ---------')
print('ต้องปูกระเบื้องทั้งหมด {} แถว'.format(total_row))
print('เหลือกระเบื้องที่ยังไม่ได้ปู {} แผ่น'.format(remain_tiles))
print('ลูกค้าต้องซื้อกระเบื้่องเพิ่ม {} แผ่น'.format(buy_more))
print('ยอดรวมทั้งหมดที่ต้องซื้อกระเบื้องเพิ่ม: {} บาท'.format(buy_more*tilecolor[color]))
#จบ EP03
