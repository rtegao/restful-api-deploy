from flask_restful import Resource, reqparse
from models.model_backend import TextPreProcessing
from models.model_backend import ModelPrediction



class ModelGatway(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument("sentences",
                        type=str,
                        required=True,
                        help="this fild can not be blank")
    
    def post(cls):
        data = ModelGatway.parse.parse_args()  

        preprocessing =  TextPreProcessing(data['sentences'])
        sentences_preprocessing = preprocessing.TextPreProcessing()

        model = ModelPrediction(original_sentences=data['sentences'],
                                preprocessed_sentence=sentences_preprocessing)
        
        return model.Prediction(),201



