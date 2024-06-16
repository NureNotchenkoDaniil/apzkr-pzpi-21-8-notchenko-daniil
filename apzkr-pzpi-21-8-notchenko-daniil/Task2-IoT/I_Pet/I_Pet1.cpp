#include <iostream>
#include <cpprest/http_client.h>
#include <cpprest/json.h>

using namespace web;
using namespace web::http;
using namespace web::http::client;

const utility::string_t BASE_URL = U("http://127.0.0.1:8000/");

int main()
{
    http_client client(BASE_URL);

    utility::string_t username = U("user1");
    utility::string_t password = U("user1");

    uri_builder builder(U("/token"));
    builder.append_query(U("username"), username);
    builder.append_query(U("password"), password);

    client.request(methods::POST, builder.to_string()).then([=](http_response response) {
        if (response.status_code() == status_codes::OK) {
            return response.extract_json();
        }
        else {
            throw std::runtime_error("Failed to obtain token");
        }
        }).then([=](json::value token_data) {

            utility::string_t access_token = token_data[U("access_token")].as_string();

            uri_builder pets_builder(U("/pets"));
            http_request request(methods::GET);
            request.headers().add(U("Authorization"), U("Bearer ") + access_token);

            return client.request(request);
            }).then([=](http_response pets_response) {
                if (pets_response.status_code() == status_codes::OK) {
                    return pets_response.extract_json();
                }
                else {
                    throw std::runtime_error("Failed to retrieve pet information");
                }
                }).then([=](json::value pets_data) {
                    std::wcout << L"Pet information:\n";
                    std::wcout << L"-----------------\n";
                    std::wcout << L"Name: " << pets_data[U("data")][0][U("pet_name")].as_string() << std::endl;
                    std::wcout << L"Breed: " << pets_data[U("data")][0][U("breed")].as_string() << std::endl;
                    std::wcout << L"Vaccinated: " << pets_data[U("data")][0][U("vaccinated")].as_bool() << std::endl;

                    }).wait();

                    return 0;
}

