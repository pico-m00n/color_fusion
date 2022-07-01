from color_fusion import ColorFusion

color1 = ColorFusion('青')
color2 = ColorFusion('赤')
color3 = ColorFusion('緑')
colors = [color1, color2, color3]

def validate(c1, c2):
    if c1 < 0 or c1 > 2:
        return False
    elif  c2 < 0 or c1 > 2:
        return False
    else:
        return True
        
def judge(c1, c2):
    if (c1 == 0 and c2 == 1) or (c1 == 1 and c2 ==0):
        return '紫'
    elif (c1 == 0 and c2 ==2) or (c1 == 2 and c2 ==0):
        return '青緑'
    elif (c1 == 1 and c2 ==2) or (c1 == 2 and c2 ==1):
        return '黄'
    else:
        return '濃' + selected_color1.name
    

print('色混ぜてみよう')
print('色一覧')
index = 1
for color in colors:
    print(str(index) + '.' + color.name)
    index += 1

color_order1 = int(input('どの色を混ぜますか？番号を入力してください：')) - 1
color_order2 = int(input('：')) - 1

selected_color1 = colors[color_order1]
selected_color2 = colors[color_order2]
    
if validate(color_order1, color_order2):
    result = judge(color_order1, color_order2)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')
    