var React = require('react');


module.exports = React.createClass({
	
	render:function(){
		var json = [
    {
        "text": "First finished step",
        "isActive": false,
        "isDone": true
    },
    {
        "text": "Second finished step",
        "isActive": false,
        "isDone": true
    },
    {
        "text": "Active step",
        "isActive": true,
        "isDone": false
    },
    {
        "text": "Unfinished step",
        "isActive": false,
        "isDone": false
    }
]; 
		return (
			<div>
				
			</div>	

		)
	}
})



