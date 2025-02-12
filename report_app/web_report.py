from flask import Flask, render_template, request
import report

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/report/')
def common_statistic():
    result = report.build_report('../data_files')
    order = request.args.get('order')
    statistic = []
    for driver, driver_result in result.items():
        place = driver_result[0]
        team = driver_result[1]
        lap_time = driver_result[2]
        statistic.append([place, driver, team, lap_time])
    if order == 'desc':
        return render_template('statistic.html', statistic=statistic[::-1])
    return render_template('statistic.html', statistic=statistic)


@app.route('/report/drivers/')
def show_drivers():
    data = report.load_data('../data_files')
    driver_id = request.args.get('driver_id')
    drivers = {}
    for driver in data:
        drivers[driver.abbreviation] = driver.name
    if driver_id:
        for driver in data:
            if driver.abbreviation == driver_id:
                driver_info = report.get_racer_info('../data_files', driver.name)
                result = driver_info.split('|')
                return render_template('driver_info.html', name=result[0],
                                       team=result[1], time=result[2])
            elif driver_id not in drivers.keys():
                return render_template('page_not_found.html')
    return render_template('drivers.html', drivers=drivers)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
