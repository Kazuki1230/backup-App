import os
import shutil
from datetime import datetime

def backup_with_timestamp(targets: list[str]):
    # 現在の日時を取得し、フォーマットする
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    for target in targets:
        try:
            # targetがフォルダの場合
            if os.path.isdir(target):
                bu_fldr_name = 'bu'
                trgt_fldr_name = f'{target.split('\\')[-1]}_{timestamp}'

                output_fldr = os.path.join(
                    os.path.dirname(target),
                    bu_fldr_name,
                    trgt_fldr_name
                )
                
                # コピー実行
                shutil.copytree(target, output_fldr)
                print(f'フォルダが {output_fldr} にコピーされました。')
                

            # targetがファイルの場合
            elif os.path.isfile(target):
                bu_fldr_name = 'bu'
                trgt_fname = os.path.basename(target).split('.')[-2]
                extension = os.path.basename(target).split('.')[-1]
                trgt_fname = trgt_fname + '_' + timestamp + '.' + extension
                # コピー先のディレクトリパスを作成
                bu_folder_path = os.path.join(os.path.dirname(target), bu_fldr_name)
                
                os.makedirs(bu_folder_path, exist_ok=True) # buフォルダを作成（存在しない場合）
                output_path = os.path.join(bu_folder_path, trgt_fname)
                # コピー実行
                shutil.copy(target, output_path)
                print(f'ファイルが {output_path} にコピーされました。')

        except Exception as e:
            if e == FileNotFoundError:
                print('ファイルまたはフォルダが見つかりません。')
                continue



# ====================================
#               DEBUG用
# ====================================
def debug():
    os.makedirs('test_fldr', exist_ok=True)
    sample_fldr = os.path.join(os.getcwd(), 'test_fldr', 'テスト用')
    sample_file = os.path.join(os.getcwd(), 'test_fldr', 'テスト用.txt')
    targets = [sample_fldr, sample_file]
    # targets = [sample_file]
    backup_with_timestamp(targets)

# debug()
