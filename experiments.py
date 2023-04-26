import os

def read_featured_experiments(files):
    experiments = []
    for filename in files:
        with open('experiments/' + filename, 'r') as f:
            title = f.readline().strip('# ')
            description = f.readline().strip()
            link = filename.replace('.md', '')
            experiments.append((title, description, link))
    return experiments

def read_all_experiments():
    """Get all experiments from the experiments folder."""
    return read_featured_experiments(sorted(os.listdir('experiments')))

def read_experiment(filename):
    """Get an experiment from the experiments folder."""
    with open('experiments/' + filename, 'r') as f:
        title = f.readline().strip('# ')
        description = f.readline().strip()
        content = []
        header = None
        c_list = []
        for line in f.read().split('\n'):
            if line:
                if '##' in line:
                    if header:
                        content.append((header, c_list))
                    header = line.strip('## ')
                    c_list = []
                else:
                    c_list.append((line.replace('* ', '') + '%').strip('1234567890. ')[:-1])
        content.append((header, c_list))
        return title, description, content