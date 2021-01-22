import os 
from PIL import Image

from webcolors import rgb_to_hex

img_url = os.path.join('../static/img/','132.jpg')

image = Image.open(img_url)

result = image.convert("P", palette=Image.ADAPTIVE, colors=10)

palette = result.getpalette()
color_counts = sorted(result.getcolors(), reverse=True)
col_sum = sum([i[0] for i in color_counts])
colors = {}
for i in range(len(color_counts)):
    palette_index = color_counts[i][1]
    ratio = color_counts[i][0] / col_sum
    dominant_color = palette[palette_index * 3: palette_index * 3 + 3]
 
            # rgb转化为二进制
    color_str = rgb_to_hex(dominant_color[:3])
 
            # key为颜色，值为所占图片的比例
    colors[str(color_str)] = ratio

print('打印下颜色',colors)
if __name__=='__main__':
    print('测试下哈哈哈')