import simplejson as json
import yaml
import os
import sys


class PathNotExistException(BaseException):
    """path for yaml or json file not exist"""


class ArgsNumError(StandardError):
    """number of arguments should be two - yaml filename and json filename"""


class FileAccessException(BaseException):
    """file not exists or dont have access"""


def get_args():
    if len(sys.argv) != 3:
        raise ArgsNumError

    yaml_file = sys.argv[1]
    if not (os.path.exists(yaml_file) and os.access(yaml_file, os.R_OK)):
        raise FileAccessException

    json_file = sys.argv[2]
    if not (os.path.exists(json_file) and os.access(json_file, os.R_OK)):
        raise FileAccessException

    yaml_path = raw_input("yaml paras path, seperate by comma: ")
    json_path = raw_input("json paras path, seperate by comma: ")

    return yaml_file, json_file, [path.strip() for path in yaml_path.split(",")], [path.strip() for path in json_path.split(",")]


def get_yaml_val(yaml_file, yaml_path):
    with open(yaml_file, "r") as fd:
        content = yaml.load(fd.read())

    for _path in yaml_path:
        if not content.get(_path, None):
            raise PathNotExistException
        content = content.get(_path)
    return content


def replace_json_file(json_file, json_key, yaml_val):
    with open(json_file, "r") as fd:
        content = json.loads(fd.read())

    search_target(content, json_key, yaml_val)

    with open("output_{filename}".format(filename=json_file), "w+") as fd:
        fd.write(json.dumps(content, indent=4))


def search_target(content, json_key, yaml_val):
    for key, val in content.items():
        if key == json_key[0] and len(json_key) == 1:
            content[key] = yaml_val
            continue

        if key == json_key[0]:
            search_target(val, json_key[1:], yaml_val)

        if type(val) == dict:
            search_target(val, json_key, yaml_val)


if __name__ == "__main__":
    yaml_file, json_file, yaml_path, json_key = get_args()
    yaml_val = get_yaml_val(yaml_file, yaml_path)
    replace_json_file(json_file, json_key, yaml_val)
