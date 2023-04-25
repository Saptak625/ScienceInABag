import os

def read_featured_experiments(files):
    experiments = []
    for filename in files:
        with open('experiments/' + filename, 'r') as f:
            title = f.readline().strip('# ')
            description = f.readline().strip()
            link = filename.strip('.md')
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
        
        for line in f.read().split('\n'):
            if line:
                print(line)
        return title, description, content