import os, shutil

def selectiveCopy(input, output, ext):
    result = os.path.abspath(output)
    print(result)
    for folName, subFolName, fileName in os.walk(input):
        for file in fileName:
            if not file.endswith(ext):
                continue
            filepath = os.path.join(os.path.abspath(folName), file)

            if not os.path.exists(result):
                os.makedirs(result)

            #prevent copying files from result folder
            if os.path.dirname(filepath) == result:
                continue
            shutil.copy(filepath, result)
            print(f'Copied {filepath} to {result}')

selectiveCopy('.',  'result', 'png')

