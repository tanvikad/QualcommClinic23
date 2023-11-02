## Steps to generate a quantized DLC file
1. To generate the ONNX file of tinyRoBERTa: in the command line, run model.py.
2. Change directory to .../snpe_docker and in the command line, run `docker run -it --rm --privileged -v "$(pwd):/workspace" --net host snpe_docker`
3. Change directory to .../snpe_docker/QualcommClinic23/Quantization_Scripts
4. To generate the DLC file of this ONNX file: in the command line, run `snpe-onnx-to-dlc -i tiny_roberta.onnx -o tiny_roberta.dlc`
5. To generate the DLC of the quantized model: in the command line, run `snpe-dlc-quantize --input_dlc tiny_roberta.dlc --input_list input_list.txt --output_dlc tiny_roberta_quantized.dlc`