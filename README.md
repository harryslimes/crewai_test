# Download Model
huggingface-cli download QuantFactory/Meta-Llama-3-8B-Instruct-GGUF Meta-Llama-3-8B-Instruct.Q8_0.gguf --local-dir downloads --local-dir-use-symlinks False

# Create ollama model
ollama create llama3-8B-instruct-q8-quantfactory -f Modelfile