## Steps to generate a quantized DLC file
1. To generate the ONNX file of tinyRoBERTa: in the command line, run model.py.
2. Change directory to .../snpe_docker and in the command line, run `docker run -it --rm --privileged -v "$(pwd):/workspace" --net host snpe_docker`
3. Change directory to .../snpe_docker/QualcommClinic23/Quantization_Scripts
4. To generate the DLC file of this ONNX file: in the command line, run `snpe-onnx-to-dlc -i <onnx-file-from-above.onnx> -o <output-file_path.dlc>`
5. TODO