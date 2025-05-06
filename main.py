from source.model_builder import ModelBuilder
from source.xml_maker import generate_config_xml
from source.json_maker import generate_meta_json


def main():
    builder = ModelBuilder("input/test_input.xml")
    model = builder.build_model()

    generate_config_xml(model, "out/config.xml")
    generate_meta_json(model, "out/meta.json")


if __name__ == "__main__":
    main()
