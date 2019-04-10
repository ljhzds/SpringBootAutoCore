import os
import time
import sys
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

from spring_auto_core.load_config import get_all_config
from spring_auto_core.auto_code import spring_gen
from spring_auto_core.utils import compress_file

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    configs = get_all_config(is_web_app=True)
    basedir = configs.get('CODE_SAVE_ROOT')
    file_dir = basedir  # 拼接成合法文件夹地址
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # 文件夹不存在就创建
    # print(file_dir)
    f = request.files['file']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f:  # 判断是否是允许上传的文件类型
        fname = f.filename
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 修改文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录

        tarfilename = new_filename.rsplit('.', 1)[0] + '.tar'
        code_save_path = spring_gen(os.path.join(file_dir, new_filename))
        print(code_save_path)
        # 打tar包
        print(os.path.join(file_dir, tarfilename))
        compress_file(os.path.join(file_dir, tarfilename), code_save_path)
        return jsonify({"errno": 0, "errmsg": "代码生成成功", 'tarfilename': tarfilename})
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})


@app.route("/download/<filename>")
def downloader(filename):
    configs = get_all_config(is_web_app=True)
    basedir = configs.get('CODE_SAVE_ROOT')
    return send_from_directory(basedir, filename, as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载


if __name__ == '__main__':
    app.run(port=5000, debug=False)
