import React, { useState, useEffect, useRef } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import { Button, Container } from '@material-ui/core';
import Box from '@material-ui/core/Box';
import PropTypes from 'prop-types';
import GenericDeleteWarning from '../../../../DeleteWarnings/GenericDeleteWarning';
/*import MaterialTable from 'material-table';
import { forwardRef } from 'react';
import { Link } from 'react-router-dom';
//import get from '../../../universalHTTPRequests/get';
//import LoadingSpinner from '../../LoadingSpinner';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import { useLocation } from 'react-router-dom';
//import { baseURL } from '../../../Constants/Config';
import AddBox from '@material-ui/icons/AddBox';
import ArrowDownward from '@material-ui/icons/ArrowDownward';
import Check from '@material-ui/icons/Check';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Clear from '@material-ui/icons/Clear';
import DeleteOutline from '@material-ui/icons/DeleteOutline';
import Edit from '@material-ui/icons/Edit';
import FirstPage from '@material-ui/icons/FirstPage';
import LastPage from '@material-ui/icons/LastPage';
import SaveAlt from '@material-ui/icons/SaveAlt';
import ViewColumn from '@material-ui/icons/ViewColumn';
import RateReviewIcon from '@material-ui/icons/RateReview';*/
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

/*const tableIcons = {
    Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
    FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
    LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
    NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    PreviousPage: forwardRef((props, ref) => (
        <ChevronLeft {...props} ref={ref} />
    )),
};*/

const useStyles = makeStyles((theme) => ({
    /*container: {
        marginTop: theme.spacing(12),
        textAlign: 'center',
    },*/
    margin: {
        margin: theme.spacing(0.5),
        marginTop: theme.spacing(0),
        width: 50,
    },
}));

QuestionField.propTypes = {
    key: PropTypes.number,
    id: PropTypes.number,
    removeQuestion: PropTypes.any.isRequired,
    question: PropTypes.string,
    response: PropTypes.string,
    summary: PropTypes.string,
    QRs: PropTypes.any,
    setQRs: PropTypes.any,
    StakeHolder_Id: PropTypes.any,
};

export default function QuestionField({
    key,
    id,
    removeQuestion,
    question,
    response,
    summary,
    QRs,
    setQRs,
    StakeHolder_Id,
}) {
    const [questionValue, setQuestionValue] = useState(question);
    const [responseValue, setResponseValue] = useState(response);
    const [summaryValue, setSummaryValue] = useState(summary);
    const stakeHolder = useRef(null);

    useEffect(() => {
        stakeHolder.current = getStakeholderInfo();
    }, []);

    /*const [didGetIssues, setDidGetIssues] = useState(false);
    //const [issues, setIssues] = useState([]);
    const issues = useRef(null);
    //let issues = [];

    const [didSetData, setDidSetData] = useState(false);
    const [cols, setColumns] = useState([]); //stores stakeholders
    const [rows, setRows] = useState([]);

    const [isLoading, setLoading] = useState(false); //stores status of whether something is loading
    var axios = require('axios'); //backend

    const [successBannerMessage, setSuccessBannerMessage] = useState(''); //success banner
    const [successBannerFade, setSuccessBannerFade] = useState(false);

    //const [issuePromises, setPromises] = useState([])
    const issuePromises = useRef(null);*/

    /*useEffect(() => {
        //stakeHolders.current = [];
        issuePromises.current = [];
        issues.current = [];
    }, []);*/

    //let issuePromises = [];

    /*useEffect(() => {
        //sets behaviour of success banner
        const timeout = setTimeout(() => {
            setSuccessBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [successBannerFade]);*/

    const [isLoading, setLoading] = useState(false);

    const [errorBannerMessage, setErrorBannerMessage] = useState(''); //error banner
    const [errorBannerFade, setErrorBannerFade] = useState(false);

    useEffect(() => {
        //sets behaviour of error banner
        const timeout = setTimeout(() => {
            setErrorBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [errorBannerFade]);

    const [currentTime, setCurrentTime] = useState(getCurrentTimeInt());
    //gets the current time in hms and converts it to an int
    function getCurrentTimeInt() {
        let d = Date();
        var h = d.substring(16, 18);
        var m = d.substring(19, 21);
        var s = d.substring(22, 24);
        return 60 * (60 * h + m) + s;
    }

    function checkTime(setTime, t) {
        var ret = false;
        //current time difference is at least 1 second, but that SHOULD be ample time for
        //the database to get back to the frontend
        if (getCurrentTimeInt() - t !== 0) {
            ret = true;
        }
        setTime(getCurrentTimeInt());
        return ret;
    }

    function updateQRs(shq, shr, shs) {
        const updatedQRs = [...QRs];
        setQRs(
            updatedQRs.map((qr) => {
                if (qr.conversation === id) {
                    qr.question = shq;
                    qr.response = shr;
                    qr.summary = shs;
                }
                return qr;
            })
        );
    }

    const onChangeQuestion = (e) => {
        setQuestionValue(e.target.value);
        updateQRs(e.target.value, responseValue, summaryValue);
    };
    //Used for delete Warning Popup window
    const [open, setOpen] = React.useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };

    const onChangeResponse = (e) => {
        setResponseValue(e.target.value);
        updateQRs(questionValue, e.target.value, summaryValue);
    };

    const onChangeSummary = (e) => {
        setSummaryValue(e.target.value);
        updateQRs(questionValue, responseValue, e.target.value);
    };

    getStakeHolderInfo();

    function getStakeholderInfo() {
        setLoading(true);

        var data = JSON.stringify({});
        var config = {
            method: 'get',
            url: baseURL + '/stakeholder?stakeholder_id=' + StakeHolder_Id, //TODO temporary endpoint -> change later
            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        };

        axios(config)
            .then(function (response) {
                setStakeHolders(response.data);
            })
            .catch(function (error) {
                setErrorBannerMessage(
                    'Failed to get Stakeholders! Please try again.'
                );
                setErrorBannerFade(true);
            });

        setLoading(false);
    }

    // <TableRow key={row.name}>
    //     <TableCell align="right">
    //         {row.issue1}
    //     </TableCell>
    //     <TableCell align="right">
    //         {row.issue2}
    //     </TableCell>
    //     <TableCell align="right">
    //         {row.issue3}
    //     </TableCell>
    //     <TableCell align="right">
    //         {row.issue4}
    //     </TableCell>
    //     <TableCell align="right">
    //         {row.issue5}
    //     </TableCell>
    // </TableRow>

    const onChange = (e, row) => {
        //TODO CHANGE TO MATCH
        if (!previous[row[issue]]) {
            setPrevious((state) => ({ ...state, [row[issue]]: row }));
        }
        const value = e.target.value;
        const name = e.target.name;
        const { id } = row[issue];
        const newRows = rows.map((row) => {
            if (row[issue] === id) {
                return { ...row, [name]: value };
            }
            return row;
        });
        setRows(newRows);
    };

    const onRevert = (id) => {
        //TODO CHANGE TO MATCH
        const newRows = rows.map((row) => {
            if (row[issue] === id) {
                return previous[id] ? previous[id] : row;
            }
            return row;
        });
        setRows(newRows);
        setPrevious((state) => {
            delete state[id];
            return state;
        });
        onToggleEditMode(id);
    };

    // const CustomTableCell = ({ row, issue, onChange }) => {
    //     const classes = useStyles();
    //     const { isEditMode } = row;
    //     return (
    //       <TableCell align="right">
    //         {isEditMode ? (
    //           <Input
    //             value={row[issue]}
    //             name={issue}
    //             onChange={e => onChange(e, row)}
    //           />
    //         ) : (
    //           row[issue]
    //         )}
    //       </TableCell>
    //     );
    //   };

    function setHeader() {
        setLoading(true);
        // let cols = [
        //     <TableCell align="right">{"Question"}</TableCell>
        // ];
        // stakeHolder.ISSUES.forEach((issue) => {
        //         cols.push(<TableCell align="right">{'Issue: ' + issue.NAME.toUpperCase()}</TableCell>)
        // });
        setLoading(false);
        return cols;
    }

    function setRows() {
        setLoading(true);
        let rows = [];

        // let question = stakeHolder.CONVERSATIONS[id](convo)
        // let issues = []
        // let allIssues = question.ISSUES;
        // allIssues.forEach((issue) => {
        //     let id = issue.ISSUE
        //     issues.push(<CustomTableCell align="right">{...{allIssues, id, onChange}}</CustomTableCell>)
        // })
        // rows.push(<TableRow key={row.name}>{issues}</TableRow>)
        // rows.unshift(<TableCell align="right">
        //     {rows[1].isEditMode ? (
        //       <>
        //         <IconButton
        //           aria-label="done"
        //           onClick={() => onToggleEditMode(row[ISSUE])}
        //         >
        //           <DoneIcon />
        //         </IconButton>
        //         <IconButton
        //           aria-label="revert"
        //           onClick={() => onRevert(row[ISSUE])}
        //         >
        //           <RevertIcon />
        //         </IconButton>
        //       </>
        //     ) : (
        //       <IconButton
        //         aria-label="delete"
        //         onClick={() => onToggleEditMode(row[ISSUE])}
        //       >
        //         <EditIcon />
        //       </IconButton>
        //     )}
        //   </TableCell>)

        setLoading(false);
        return rows;
    }

    const classes = useStyles();

    return (
        <div>
            <Box
                display="flex"
                flexDirection="row"
                p={1}
                m={1}
                bgcolor="background.paper"
            >
                <Box p={1}>
                    <TextField
                        style={{ width: 700 }}
                        id="outlined-multiline-static"
                        label="Question"
                        multiline
                        rows={2}
                        variant="outlined"
                        value={questionValue}
                        onChange={onChangeQuestion}
                    />
                    <TextField
                        style={{ width: 700, marginTop: 20 }}
                        id="outlined-multiline-static"
                        label="StakeHolder Response"
                        multiline
                        rows={2}
                        variant="outlined"
                        value={responseValue}
                        onChange={onChangeResponse}
                    />
                    <TextField
                        style={{ width: 700, marginTop: 20 }}
                        id="outlined-multiline-static"
                        label="Q &amp; A Summary"
                        multiline
                        rows={2}
                        variant="outlined"
                        value={summaryValue}
                        onChange={onChangeSummary}
                    />
                    <TableContainer
                        component={Paper}
                        style={{ width: 700, marginTop: 20 }}
                    >
                        <Table
                            className={classes.table}
                            size="small"
                            aria-label="a dense table"
                        >
                            <TableHead>
                                <TableRow>{setHeader()}</TableRow>
                            </TableHead>
                            <TableBody>{setRows()}</TableBody>
                        </Table>
                    </TableContainer>
                </Box>
                <Box p={1}>
                    <Button
                        className={classes.margin}
                        variant="contained"
                        color="primary"
                        onClick={handleClickOpen}
                    >
                        Delete
                    </Button>

                    <GenericDeleteWarning
                        remove={() => removeQuestion(id)}
                        open={open}
                        setOpen={setOpen}
                    />
                </Box>
            </Box>
        </div>
    );
}
