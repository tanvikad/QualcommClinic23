## Steps to generate a quantized DLC file and test it
1. Set torch version to 2.1.0 in Dockerfile. (Otherwise, run `pip install --upgrade torch` in the terminal/command line.)
1. To generate the ONNX file of tinyRoBERTa: in the command line, run model.py (i.e., `python model.py`).
2. Change directory to .../snpe_docker and in the command line, run `docker run -it --rm --privileged -v "$(pwd):/workspace" --net host snpe_docker`
3. Change directory to .../snpe_docker/QualcommClinic23/Quantization_Scripts
4. To generate the DLC file of this ONNX file: in the command line, run `snpe-onnx-to-dlc -i tiny_roberta.onnx -o tiny_roberta.dlc`
5. To generate the DLC of the quantized model: in the command line, run `snpe-dlc-quantize --input_dlc tiny_roberta.dlc --input_list input_list.txt --output_dlc tiny_roberta_quantized.dlc`
6. To test that the DLC works, run `snpe-net-run --container tiny_roberta_quantized.dlc --input_list input_list.txt`