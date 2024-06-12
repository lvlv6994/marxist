from manim import *
import geopandas as gpd
import matplotlib.pyplot as plt

class DrawMap(Scene):
    def construct(self):
        # 读取 GeoJSON 文件
        gdf = gpd.read_file("china.topo.json")
        
        # 创建一个 Matplotlib 图形
        fig, ax = plt.subplots()
        
        # 绘制 GeoDataFrame
        gdf.plot(ax=ax, color='lightblue', edgecolor='black')
        
        # 保存图形为 PNG 图片
        plt.savefig("china_map.png", dpi=300)
        
        # 将 PNG 图片导入 Manim
        map_image = ImageMobject("china_map.png")
        
        # 调整图片大小和位置
        map_image.scale(2).to_edge(UP)
        
        # 在场景中添加图片
        self.add(map_image)

if __name__ == "__main__":
    from manim import *
    config.background_color = WHITE
    scene = DrawMap()
    scene.render()
