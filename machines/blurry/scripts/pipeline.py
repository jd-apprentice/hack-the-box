from clearml import *

@PipelineDecorator.pipeline(
    name='pipe',
    project='sample',
    version='0.1'
)

executing_pipeline(pickle_url='https://example.com/iris_dataset.pkl')