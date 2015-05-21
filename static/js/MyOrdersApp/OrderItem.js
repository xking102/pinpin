var React = require("react");


module.exports = React.createClass({
	render:function(){
        console.log('begin');
        console.log(this.props.id);
        console.log(this.props.gid);
        console.log(this.props.price);
        console.log('end');
		return(
			<div>
                <div className="row-fluid">
                    <div className="span3 center">1</div>
                    <div className="span3 center">dfadf</div>
                    <div className="span3 center">123</div>
                    <div className="span3 center">
                        <a className="btn btn-success" href="#">
                            <i className="halflings-icon white zoom-in"></i>
                        </a>
                        <a className="btn btn-danger" href="#">
                            <i className="halflings-icon white trash"></i>
                        </a>
                    </div>
                </div>
            </div>

		)		
	}
})