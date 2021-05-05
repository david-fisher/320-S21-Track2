import React, { useEffect, useRef, useState } from 'react';
import Chart from 'chart.js';
import { BASE_URL, STUDENT_ID } from '../../constants/config';


function Radar(props) {
    const chartContainer = useRef(null);
    const [chartInstance, setChartInstance] = useState(null);
    const [sName, setSName] = useState("");
    const [coverage, setCoverage] = useState({});
    // state for input

    const chartConfig = onChartChange()

    useEffect (() => {
        fetch(`${BASE_URL}/students/`)
        .then(res => res.json())
        .then(studentData => {
            let s = studentData.results.filter(r => r.student === STUDENT_ID)[0]
            setSName(s.fname + " " + s.lname)
            
        })
        .catch(err => {
            console.log(err)
        })
      }, [])

    useEffect (() => {
        fetch(`${BASE_URL}/get_issues/?scenario_id=${props.match.params.sid}`)
        .then(res => res.json())
        .then(issueData => {
            console.log(issueData)
            let newCoverage = {}
            issueData
            .forEach(issue => {
            newCoverage[issue.name] = issue.importance_score
            })
            setCoverage(newCoverage)
            
        })
        .catch(err => {
            console.log(err)
        })
    }, [])

    useEffect(() => {
        // if (chartContainer && chartContainer.current) {
        const newChartInstance = new Chart(chartContainer.current, chartConfig);
        setChartInstance(newChartInstance);
         //}
     }, [coverage, sName]);

    return (
        <canvas
            ref={chartContainer}
            id="coverage-plot"
        />
    )
    

    // function colorLimit(value) {
    //     if (value < 1.5) {
    //         return "rgba(255, 0, 0, 0.2)"
    //     }
    //     else if (value < 2.5) {
    //         return "rgba(255, 255, 0, 0.2)"
    //     }
    //     else {
    //         return "rgba(0, 128, 0, 0.2)"
    //     }
    // }

    function onChartChange() {
        let Coverage = coverage //{ Safety: 0.5, Salary: 0.667, Reputation: 2.0, Privacy: 0.8 };
        console.log("Name: " + sName)
        console.log(coverage)
        return {
            type: 'radar',
            data: {
                //labels: coverage.keys,
                labels: Object.keys(coverage).map(x => x + "(importance score: " + coverage[x] + ")"),
                datasets: [{
                    label: sName,
                    backgroundColor: "rgba(255, 255, 0, 0.2)",
                    data: Object.values(coverage)
                }]
            },
            options: {
                scale: {
                    ticks: {
                        beginAtZero: true,
                        min: 0,
                        display: false
                    },
                    pointLabels: {
                        fontSize: 15,
                        display: true
                    },
                },
                legend: {
                    display: true,
                    labels: {
                        fontSize: 20
                    }
                }
            }
        }
    }
}

export default Radar;
