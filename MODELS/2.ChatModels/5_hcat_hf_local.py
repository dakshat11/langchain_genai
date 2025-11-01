from langchain_huggingface import HuggingFaceChatModel
model = HuggingFaceChatModel(model_name="hcat-hf-local", model_kwargs={"device": "cpu"})
response = model.predict_messages([{"role": "user", "content": "Hello world!"}])
print(response.content) 
