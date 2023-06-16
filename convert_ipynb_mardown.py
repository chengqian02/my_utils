from nbconvert import MarkdownExporter
import nbformat
import argparse
import os

def convert_ipynb_to_md(input_folder, output_folder, exclude_files=[], single_file=False):
    """
    将输入文件夹中的所有.ipynb文件转换为输出文件夹中的对应.md文件。

    参数：
    - input_folder：包含要转换的.ipynb文件的文件夹的路径。
    - output_folder：输出转换后的.md文件的文件夹的路径。
    - exclude_files：要排除的文件列表，这些文件不进行转换。
    - single_file: 是否转为单一文件
    """

    # 创建MarkdownExporter对象
    exporter = MarkdownExporter()
    file_list = []
    # 遍历输入文件夹中的所有.ipynb文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.ipynb'):
            file_path = os.path.abspath(os.path.join(input_folder, file_name))
            if os.path.basename(file_path) in exclude_files:
                continue

            # 构建输入和输出文件的路径
            input_path = file_path
            output_path = os.path.abspath(os.path.join(output_folder, file_name.replace('.ipynb', '.md')))

            try:
                # 使用nbformat将.ipynb文件转换为Notebook节点对象
                with open(input_path, 'r', encoding='utf-8') as f:
                    nb = nbformat.read(f, as_version=4)

                # 使用MarkdownExporter将Notebook节点对象转换为.md文件
                body, _ = exporter.from_notebook_node(nb)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(body)

                if single_file:
                    file_list.append(output_path)
                print(f'Converted {input_path} to {output_path}')

            except Exception as e:
                print(f'Error processing {input_path}: {str(e)}')

    if single_file:
        merge_md_files(files=file_list, output_name=output_name)
        for file_name in file_list:
            os.remove(file_name)


def merge_md_files(files, output_name):
    """
    将输入文件夹中的所有.md文件合并为一个.md文件。

    参数：
    - input_folder：包含要合并的.md文件的文件夹的路径。
    - output_path：输出合并后的.md文件的路径。
    """
    # 遍历输入文件夹中的所有.md文件，将它们合并为一个字符串
    error_list = []
    merged_md = ''
    for file_name in files:
        if os.path.basename(file_name).endswith('.md'):
            file_path = os.path.abspath(file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                merged_md += f.read()
        else:
            error_list.append(file_name)
    # 将合并后的字符串写入输出文件
    with open(output_name, 'w', encoding='utf-8') as f:
        f.write(merged_md)
    if error_list:
        print("这些文件不合格",error_list)

if __name__ == '__main__':
    # 创建ArgumentParser对象
    parser = argparse.ArgumentParser(description='Convert and merge Jupyter Notebook files')
    # 添加命令行参数，使用 metavar 参数指定希望显示的参数名称，使用 dest 参数将参数名映射到单个字符
    parser.add_argument('-i', '--input_folder', metavar='INPUT_FOLDER',default=os.getcwd(),
                        help='the folder containing the Jupyter Notebook files')
    parser.add_argument('-o', '--output_folder', metavar='OUTPUT_FOLDER',default=os.getcwd(),
                        help='the folder to store the converted Markdown files')
    parser.add_argument('-p', '--output_name', metavar='OUTPUT_NAME', default='merge.md',
                        help='the path to the merged Markdown file')
    parser.add_argument('-e', '--exclude', nargs='+', default=[],
                        help='the list of files to exclude from conversion')
    parser.add_argument('-s', '--single_file', metavar='SINGLE_FILE', nargs='?', const='True',
                        help='the path to the single converted Markdown file')
    parser.add_argument('-f', '--files',metavar='FILES', nargs='+', default=[],
                        help='the list of files to convert')
    # 解析命令行参数
    args = parser.parse_args()

    # 检查是否同时使用了 -i 和 -f 参数
    if args.input_folder != os.getcwd() and len(args.files) > 0:
        parser.error("-i and -f cannot be used together")

    # 将输入文件夹和排除文件列表中的相对路径转换为绝对路径
    input_folder = os.path.abspath(args.input_folder)
    output_folder = os.path.abspath(args.output_folder)
    exclude_files = [os.path.basename(exclude_file) for exclude_file in args.exclude]
    output_name = os.path.abspath(os.path.join(args.output_folder,args.output_name))
    # 判断是否需要转换为单一文件
    if not args.single_file:
        single_file = False
    convert_ipynb_to_md(input_folder, output_folder, exclude_files=exclude_files, single_file=args.single_file)

    # 判断是否需要合并某些文件列表
    if args.files:
        files = [os.path.abspath(file) for file in args.files]
        merge_md_files(files, output_name)