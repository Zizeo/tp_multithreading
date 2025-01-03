#include <cpr/cpr.h>

#include <Eigen/Dense>
#include <chrono>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>

class Task {
public:
    int identifier;
    int size;
    double time;
    Eigen::MatrixXd a;
    Eigen::VectorXd b;
    Eigen::VectorXd x;

    Task(int identifier = 0, int size = rand() % 9000 + 1000)
        : identifier(identifier)
        , size(size ? size : rand() % 9000 + 1000)
        , time(0)
    {
        a.resize(this->size, this->size);
        b.resize(this->size);
        x.resize(this->size);
        x.setZero(this->size);
        a.setRandom(this->size, this->size);
        b.setRandom(this->size);
        time = 0;
    }

    void work()
    {
        auto start = std::chrono::steady_clock::now();
        x = a.ldlt().solve(b);
        auto finish = std::chrono::steady_clock::now();
        time = std::chrono::duration_cast<std::chrono::duration<double>>(finish - start)
                   .count();
    }

    auto to_json()
    {
        using namespace nlohmann;
        json j;
        j["identifier"] = std::to_string(identifier);
        j["size"] = std::to_string(size);
        j["time"] = std::to_string(time);
        auto matrix_array = json::array();
        for (int i = 0; i < size; i++) {
            auto row = json::array();
            for (int j = 0; j < size; j++) {
                // printf("\n test \n");
                row.push_back(a(i, j));
                // printf("\n test \n");
            }
            matrix_array.push_back(row);
        }
        j["a"] = matrix_array;

        auto b_array = json::array();
        auto x_array = json::array();
        for (int i = 0; i < size; i++) {
            b_array.push_back(b(i));
            x_array.push_back(x(i));
        }
        j["b"] = b_array;
        j["x"] = x_array;

        return j;
    }

    static Task from_json(const std::string& json_str)
    {
        using namespace nlohmann;
        auto j = json::parse(json_str);
        Task task(j["identifier"], j["size"]);

        auto& matrix_array = j["a"];
        for (int i = 0; i < task.size; i++) {
            for (int j = 0; j < task.size; j++) {
                task.a(i, j) = matrix_array[i][j];
            }
        }
        auto& b_array = j["b"];
        auto& x_array = j["x"];
        for (int i = 0; i < task.size; i++) {
            task.b(i) = b_array[i];
            task.x(i) = x_array[i];
        }

        return task;
    }

    bool operator==(const Task& other) const
    {
        return identifier == other.identifier && size == other.size && a.isApprox(other.a) && b.isApprox(other.b) && x.isApprox(other.x);
    }

    std::string read_server()
    {
        while (true) {
            auto response = cpr::Get(cpr::Url { "http://localhost:8000/" });
            if (response.status_code == 200 && response.text != "") {
                return response.text;
            }
        }
    }

    void write_server(nlohmann::json j)
    {
        auto response = cpr::Post(cpr::Url { "http://localhost:8000/" }, cpr::Body { j.dump() },
            cpr::Header { { "Content-Type", "application/json" } });

        if (response.status_code == 200) {
            std::cout << "Success: " << response.text << std::endl;
        } else {
            std::cout << "Error " << response.status_code << ": " << response.text
                      << std::endl;
        }
    }
};

int main()
{
    while (true) {
        Task task;
        std::string json_str = task.read_server();
        if (json_str != "") {
            task = Task::from_json(json_str);
        }
        task.work();
        task.write_server(task.to_json());
    }
    return 0;
}
