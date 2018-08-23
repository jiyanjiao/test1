from urllib import request
import re
import pymysql
class MovieTop(object):
    def __init__(self):
        self.start = 0
        self.param = '&filter='
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        self.movie_list = []
        self.file_path = 'D:\movie_spider.txt'
    '''
    第一页:https://movie.douban.com/top250?start=0&filter=
    第二页:https://movie.douban.com/top250?start=25&filter=
    第三页: https://movie.douban.com/top250?start=50&filter=
    第四页: https://movie.douban.com/top250?start=75&filter=
    第五页: https://movie.douban.com/top250?start=100&filter=
    
    '''
    def get_page(self):
        page_content = ''
        try:
            url = 'https://movie.douban.com/top250?start='+str(self.start)
            req = request.Request(url,headers= self.headers)
            response = request.urlopen(req)
            page = response.read().decode('utf-8')
            page_num  = (self.start +25)//25
            print('正在抓取第'+str(page_num)+'页数据......')
            self.start +=25
            #print('page_content值为',page)
            return page
        except request.URLError as e:
            if hasattr(e,'reason'):
                print('抓取失败,失败原因:',e.reason)

    def get_movie_info(self):
        pattern = re.compile('<div.*?class="item">.*?'
                             + '<div.*?class="pic">.*?'
                             + '<em.*?class="">(.*?)</em>'
                             + '<div.*?class="info">.*?'
                             + '<span.*?class="title">(.*?)'
                             + '</span>.*?<span.*?class="title">(.*?)</span>.*?'
                             + '<span.*?class="other">(.*?)</span>.*?</a>.*?'
                             + '<div.*?class="bd">.*?<p.*?class="">.*?'
                             + '导演:(.*?)&nbsp;&nbsp;&nbsp;.*?</br>'
                             + '(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;'
                             + '(.*?)</p>.*?<div.*?class="star">.*?'
                             + '<span.*?'
                             + 'class="rating_num".*?property="v:average">'
                             + '(.*?)</sapn>.*?'
                             + '.*?<span>(.*?)人评价</span>.*?'
                             + '<p.*?class="quote">.*?'
                             + '<span.*?class="inq">(.*?)'
                             + '</span>.*?</p>',re.S)
        while self.start <= 225:
            page = self.get_page()
            movies = re.findall(pattern, page)
            for movie in movies:
                self.movie_list.append([movie[0],
                                        movie[1],
                                        movie[2].lstrip('&nbsp;/&nbsp'),
                                        movie[3].lstrip('&nbsp;/nbsp'),
                                        movie[4],
                                        movie[5].lstrip(),
                                        movie[6],
                                        movie[7].rstrip(),
                                        movie[8],
                                        movie[9],
                                        movie[10]])
                print('movie_list的值为:',movie)

    def write_text(self):
        print('开始向文件写入数据......')
        file_top = open(self.file_path,'w',encoding='utf-8')
        try:
            for movie in self.movie_list:
                file_top.write('电影排名:'+movie[0]+'\r\n')
                file_top.write('电影名称:'+movie[1]+'\r\n')
                file_top.write('外文名称:'+movie[2]+'\r\n')
                file_top.write('电影别名:',movie[3]+"\r\n")
                file_top.write('导演姓名:',movie[4] + "\r\n")
                file_top.write('上映年份:',movie[5] + "\r\n")
                file_top.write('制作国家/地区:', movie[6] + "\r\n")
                file_top.write('电影类别:', movie[7] + "\r\n")
                file_top.write('电影评分:', movie[8] + "\r\n")
                file_top.write('参评人数:', movie[9] + "\r\n")
                file_top.write('简短影评:', movie[10] + "\r\n\r\n")
                print('抓取结果写入文件成功....')
        except Exception as e:
            print(e)
        finally:
            file_top.close()

    def upload(self):
        db = pymysql.connect("localhost", "root", "123456", "PythonTest", charset='utf8')
        cursor = db.cursor()

        insertStr = "INSERT INTO doubanTop250(rankey, name, alias, director," \
                    "showYear, makeCountry, movieType, movieScore, scoreNum, shortFilm)" \
                    "VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', %f, %d, '%s')"

        try:
            for movie in self.movieList:
                insertSQL = insertStr % (int(movie[0]), str(movie[1]), str(movie[2]), str(movie[3]),
                                         str(movie[4]), str(movie[5]), str(movie[6]), float(movie[7]),
                                         int(movie[8]), str(movie[9]))
                cursor.execute(insertSQL)
            db.commit()
            print('成功上传至数据库...')
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()

if __name__ == '__main__':
    mt = MovieTop()
    #mt.get_page()
    mt.get_movie_info()
    mt.write_text()
    print('数据抓取完毕')
    print('开始从豆瓣电影抓取数据.......')
    print('数据抓取完毕')
    mt.upload()