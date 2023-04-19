use Dancer;

get '/hello' => sub {
    return "Hello, World!";
};

dance;
