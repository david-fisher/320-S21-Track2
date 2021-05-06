import React, { useEffect, useRef, useState } from 'react';
import Chart from 'chart.js';
import { BASE_URL, STUDENT_ID } from '../../constants/config';


function Radar(props) {
    const chartContainer = useRef(null);
    const [chartInstance, setChartInstance] = useState(null);
    const [sName, setSName] = useState("");
    const [importance, setImportance] = useState({});
    const [score, setScore] = useState({});
    const [total, setTotal] = useState({});
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
            let newImportance = {}
            issueData
            .forEach(issue => {
            newImportance[issue.name] = issue.importance_score
            })
            setImportance(newImportance)
            
        })
        .catch(err => {
            console.log(err)
        })
    }, [])

    useEffect(() => {
        fetch(`${BASE_URL}/get_issueRadarPlotTotal/?scenario_id=${props.match.params.sid}`)
        .then(res => res.json())
        .then(totalData => {
            setTotal(totalData)
        })
    }, [])

    useEffect(() => {
        fetch(`${BASE_URL}/get_issuesScores/?student_id=${STUDENT_ID}&scenario_id=${props.match.params.sid}`)
        .then(res => res.json())
        .then(scoreData => {
            setScore(scoreData)
        })
    }, [total])

    useEffect(() => {
        // if (chartContainer && chartContainer.current) {
        const newChartInstance = new Chart(chartContainer.current, chartConfig);
        setChartInstance(newChartInstance);
         //}
     }, [importance, sName, score, total]);

    return (
        <canvas
            ref={chartContainer}
            id="importance-plot"
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
        return {
            type: 'radar',
            data: {
                labels: Object.keys(total).map(x => x + "(importance score: " + importance[x] + ")"),
                datasets: [{
                    label: sName,
                    backgroundColor: "rgba(255, 255, 0, 0.2)",
                    data: Object.keys(total).map(x => ((score[x]/total[x]).toFixed(2))*100)
                }]
            },
            options: {
                scale: {
                    ticks: {
                        beginAtZero: true,
                        min: 0,
                        max: 100,
                        callback: function(value, index, values) {
                            return value + '%';
                        }
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
