# python script

def convert_to_markdown(metrics_dict):
    markdown = ""
    for k in metrics_dict.keys():
        markdown += f"## {k} %0A%0A"

        # format headers
        headers = "|"
        for nam in metrics_dict[k].keys():
            headers += f" {nam} "
        markdown += headers + "%0A"

        # add lines under headers
        markdown += "|" + " -- |" * len(metrics_dict[k]) + "%0A"

        # add values
        metrics = "|"
        for val in metrics_dict[k].values():
            try:
                val = float(val)
                metrics += f" {val:.3} |"
            except ValueError:
                metrics += f" {val} |"
        markdown += metrics + "%0A"

    return markdown

if __name__ == "__main__":
    run_metrics = {'GitHubActionExperiment_1585169537_0149ea05': {'Kernel type': 'linear', 'Penalty': 1.0, 'Accuracy': 0.9333333333333333, 'precision': 0.9333333333333333, 'recall': 0.9333333333333333, 'f1-score': 0.9333333333333333, 'confusion_matrix': 'aml://artifactId/ExperimentRun/dcid.GitHubActionExperiment_1585169537_0149ea05/confusion_matrix', 'confusion_matrix_unnormalized': 'aml://artifactId/ExperimentRun/dcid.GitHubActionExperiment_1585169537_0149ea05/confusion_matrix_unnormalized_1585170650.png', 'confusion_matrix_normalized': 'aml://artifactId/ExperimentRun/dcid.GitHubActionExperiment_1585169537_0149ea05/confusion_matrix_normalized_1585170651.png', 'Model Name': 'model.pkl'}}
    metrics_markdown = convert_to_markdown(run_metrics)
    print(f"::set-output name=run_metrics::{metrics_markdown}")