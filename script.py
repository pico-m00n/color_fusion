from color_fusion import ColorFusion

color1 = ColorFusion('青')
color2 = ColorFusion('赤')
color3 = ColorFusion('緑')
colors = [color1, color2, color3]

def validate(color_order1, color_order2):
    if (color_order1 or color_order2) < 0 or (color_order1 or color_order2) > 2:
        return True
    else:
        return False
    


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
    if selected_color1 == color1 and selected_color2 == color2:
        print("紫")
    elif selected_color1 == color1 and selected_color2 == color3:
        print('青緑')
    elif selected_color1 == color2 and selected_color2 == color1:
        print('紫')
    elif selected_color1 == color2 and selected_color2 == color3:
        print('黄')
    elif selected_color1 == color3 and selected_color2 == color1:
        print('青緑')
    elif selected_color1 == color3 and selected_color2 == color2:
        print('青緑')
    else:
        print('濃' + selected_color1.name)
else:
    print('正しい数字を入力してください')
    