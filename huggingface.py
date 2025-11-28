from huggingface_hub import create_repo
from huggingface_hub import HfApi, upload_folder

name = "results_weightCE"
create_repo(name, private=False)

api = HfApi()

upload_folder(
    folder_path=f"summary_result/{name}",            # your model folder
    repo_id=f"cppmai/{name}",
    repo_type="model"
)
