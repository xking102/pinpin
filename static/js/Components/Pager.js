var React = require('react');


module.exports = React.createClass({
	render:function(){
		var NextBtn = (<div/>);
		if(this.props.hasNext){
			NextBtn = (
				<button onClick={this.props.onClickNext}>{'下一页'}</button>
			);
		}
		var PrevBtn = (<div/>);
		if(this.props.hasPrev){
			PrevBtn = (
				<button onClick={this.props.onClickPrev}>{'上一页'}</button>
			);
		}
		return(
			<div style={{marginLeft:'45%'}}>
				{PrevBtn}{NextBtn}
			</div>
		)
	}
})